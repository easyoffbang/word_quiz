import json

from django.shortcuts import render, resolve_url


words = {
    "hello": "used as a greeting when you meet somebody, when you answer the telephone or when you want to attract somebody’s attention",
    "ninja": "a person trained in traditional Japanese skills of fighting and moving quietly",
    "owl": "a bird of prey (= a bird that kills other creatures for food) with large round eyes, that hunts at night. Owls are traditionally thought to be wise.",
    "programmer": "a person whose job is writing programs for computers",
    "laptop": "a small computer that can work with a battery and be easily carried"
}

def start_page(request):
    return render(request, 'index.html')

def word_test(request, step):
    name = request.GET.get('name')
    answer = request.GET.get('answer')
    answer_list = request.GET.get('answer_list') or '[]'

    answer_list = json.loads(answer_list)

    if step > 1:
        answer_list.append(answer)

    next_url = resolve_url('test', (step + 1),)

    if step ==len(words):
        next_url = resolve_url('result')

    context = {
        'name': name,
        'step': step,
        'meaning': list(words.values())[step - 1],
        'next_url': next_url,
        'answer_list': json.dumps(answer_list, ensure_ascii=False)
    }

    return render(request, "test.html", context)  #html파일과 연결

def result(request):
    name = request.GET.get('name')
    answer = request.GET.get('answer')
    answer_list = request.GET.get('answer_list') or '[]'

    answer_list = json.loads(answer_list)
    answer_list.append(answer)

    check_answer_list = {word: answer_list[index] for index, word in enumerate(words.keys())}                                  #사용자와 답안 비교를 위한 딕셔너리 만듦{답안:사용자가입력한답}
    print(check_answer_list)

    context = {
        'name': name,
        'check_answer_list': check_answer_list,
    }

    return render(request, "result.html", context)
