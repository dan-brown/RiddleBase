from django.http import Http404, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from riddles.models import RiddleState
from sudoku.models import Sudoku


def index(request):
    return render(request, 'sudoku/index.html', {
        'ids': list(sudoku.id for sudoku in Sudoku.objects.all()),
    })


def riddle(request, riddle_id):
    try:
        sudoku = Sudoku.objects.get(pk=riddle_id)
    except Sudoku.DoesNotExist:
        raise Http404("Sudoku does not exist")

    state_values = sudoku.pattern
    if request.user.is_authenticated():
        states = RiddleState.objects.filter(user=request.user, riddle=sudoku)
        if len(states) is 1:
            state_values = states[0].values
        elif len(states) is 0:
            state = RiddleState(user=request.user, riddle=sudoku, values=sudoku.pattern)
            state.save()
            state_values = state.values

    return render(request, 'sudoku/riddle.html', {
        'riddle_type': 'Riddle',
        'riddle_id': sudoku.id,
        'pattern': sudoku.pattern,
        'state': state_values,
        'box_rows': sudoku.box_rows,
        'previous_id': sudoku.previous_id(),
        'next_id': sudoku.next_id(),
    })


@csrf_exempt
@require_POST
def check(request, riddle_id):
    try:
        sudoku = Sudoku.objects.get(pk=riddle_id)
    except Sudoku.DoesNotExist:
        raise Http404("Sudoku does not exist")

    proposal = request.POST.get("proposal")
    correct = proposal is not None and proposal == sudoku.solution
    response = {'correct': correct}
    return JsonResponse(response)


def creator(request):
    return render(request, 'sudoku/creator.html')


@require_POST
def create(request):
    error = []
    if not request.user.has_perm("riddles.add_sudoku"):
        error.append("no permission")

    solution = request.POST.get("solution")
    pattern = request.POST.get("pattern")

    if solution is None:
        error.append("no solution")
    if pattern is None:
        error.append("no pattern")

    if error:
        return JsonResponse({'error': error})

    created = Sudoku(solution=solution,
                     pattern=pattern,
                     state=pattern,
                     difficulty=5,
                     box_rows=3)
    created.save()
    return JsonResponse({'id': created.id})