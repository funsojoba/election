from django.shortcuts import render
from django.db import connection


def index(request):
    cursor = connection.cursor()
    lga_sql = "SELECT lga_name, lga_id FROM lga"
    cursor.execute(lga_sql)
    data = cursor.fetchall()

    context = {
        "name": data,
    }
    return render(request, 'results_app/index.html', context)


def get_lga(request, pk):
    cursor = connection.cursor()
    results = "SELECT party_abbreviation, party_score FROM announced_lga_results WHERE lga_name = "+pk+""
    # local_gvt = "SELECT lga_name FROM lga WHERE lga_id = "+pk+""

    # cursor.execute(local_gvt)
    cursor.execute(results)
    results = cursor.fetchall()
    context = {"result": results}
    print(results)
    return render(request, 'results_app/lga_results.html', context)
