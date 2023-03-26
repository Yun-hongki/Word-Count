from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, 'main.html')

def result(request):
    text = request.GET["text"]
    text_list = text.split()
    final_list = []
    for i in text_list:
        final_list.append(i.lower())
    text_dict = {}
    for word in final_list:
        if word in text_dict:
            text_dict[word] += 1
        else:
            text_dict[word] = 1
    words = sorted(text_dict.items(), key=lambda x:x[1], reverse=True)
    values = 0
    for key, value in words:
        values = values + int(value)

    return render(request, 'result.html', {'words' : words, 'values' : values})