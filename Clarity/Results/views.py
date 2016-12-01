from django.shortcuts import render
from os import listdir

# Create your views here.

def calcScore(parse_file):
    contents = open(parse_file, "r")

def results(request):

    if request.method == "POST":
        query = request.POST.get("search")		
        sp_query = query.split()
        path = "/Users/sireesh/Documents/School/11B/Computers/clarity/Clarity/Results/subs/"
        sub_buf  = []
        sub_files = listdir(path)
        parsed_subs = []
        max_score = 0
        best_file = ""

        for i in sub_files:
            sub_path = path + i
            contents = open(sub_path, "r")
            cont_str = contents.read()
            sub_contents = cont_str.split()
            score = 0
            for j in sub_contents:
                if j in sp_query:
                    score += 1
            if score > max_score:
                max_score = score
                best_file = sub_path
        f = open(best_file, 'r')
        sub_lines = f.readlines()
        return render(request, 'Results/index.html', {'best_hit': best_file})
    else:
        return render(request, 'Results/index.html', {})
