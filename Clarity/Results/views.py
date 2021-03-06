from django.shortcuts import render
from os import listdir
import os

# Create your views here.

def results(request):

    if request.method == "POST":
        query = request.POST.get("search")		
        query = query.lower()
        sp_query = query.split()
        print(sp_query)
        path = os.path.dirname(os.path.abspath(__file__)) + "/subs/"
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
                j = j.lower()
                if j in sp_query:
                    score += 1
            if score > max_score:
                max_score = score
                best_file = sub_path
        maxlineno = 0
        if best_file != "":
            f = open(best_file, 'r')
            sub_lines = f.readlines()
            max_score = 0
            line = ""
            lineno = 0
            for i in sub_lines:
                lineno += 1
                score = 0
                words = i.split()
                for j in words:
                    if j in sp_query:
                        score += 1
                if score > max_score:
                    max_score = score
                    line = i
                    maxlineno = lineno
            for i in range(2,10): 
                ists = not any(j.isalpha() for j in sub_lines[maxlineno - i])
                if ists:
                    line = sub_lines[maxlineno - i]
                    break

            pos = 0
            yturl = ""
            for i in best_file:
                if i == '-':
                    yturl = best_file[pos+1:len(best_file) - 7]
                pos += 1

            line = line.replace('.', ':')
            ts_spl = line.split(":")
            print(ts_spl, line)
            time = ts_spl[0] + "h" + ts_spl[1] + "m" + ts_spl[2] + "s"

            return render(request, 'Results/index.html', {'best_hit': best_file[len(path):len(best_file) - 8 - len(yturl)], 'line': line, 'yturl': "https://youtu.be/" + yturl + "?t=" +  time})
        else :
            return render(request, 'Results/index.html', {'best_hit': "Term not found"})
    else:
        return render(request, 'Results/index.html', {})
