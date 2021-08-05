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
    data = "SELECT polling_unit_id, polling_unit_name FROM polling_unit WHERE lga_id = "+pk+""

    first_data = cursor.execute(data)
    results = first_data.fetchall()

    total_votes = "SELECT party_abbreviation, party_score FROM announced_lga_results WHERE lga_name = "+pk+""
    second_data = cursor.execute(total_votes)
    second_result = second_data.fetchall()
    
    context = {"result": results, "votes": second_result}
    return render(request, 'results_app/lga_results.html', context)


def get_pu(request, pk):
    cursor = connection.cursor()
    data = "SELECT party_abbreviation, party_score FROM announced_pu_results WHERE polling_unit_uniqueid = "+pk+""
    cursor.execute(data)
    result = cursor.fetchall()
    context = {"result": result}
    print(result)
    return render(request, 'results_app/pu_results.html', context)
