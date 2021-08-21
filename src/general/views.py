from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
from .models import Agent, Buyer, Owner, Property

from collections import namedtuple


def namedtuplefetchall(cursor):
    "Return all rows from a cursor as a namedtuple"
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]

# Create your views here.


def index(request):
    return render(request, 'general/index.html', {})


def loga(request):
    cursor = connection.cursor()

    if request.method == 'POST':
        name = request.POST.get('user')
        pwd = request.POST.get('pwd')

        cursor.execute("SELECT agentid,password FROM agent;")

        li = []
        for i in cursor:
            li.append(i)

        pwd = str(pwd)
        name = str(name)

        flag = 0
        for e, j in li:
            e = str(e)
            if e == name and j == pwd:
                flag = 1
                break

        if flag == 1:
            cursor.execute("SELECT * FROM agent WHERE agentid = " + name + ";")
            ld = []
            for j in cursor:
                ld.append(j)
            print(ld)

            cursor.execute(
                "SELECT propertyid, ownerid, status, date_sold FROM property NATURAL JOIN agent WHERE agent.agentid = " + name + ";")
            cards = []
            for x in cursor:
                cards.append(x)
            print(cards)
            context = {
                "agentdata": ld,
                "carddata": cards,
            }
            return render(request, 'general/agent.html', context)
        else:
            return render(request, 'general/logina.html', {})
    else:
        return render(request, 'general/logina.html', {})


def logb(request):
    cursor = connection.cursor()

    if request.method == 'POST':
        name = request.POST.get('user')
        pwd = request.POST.get('pwd')

        cursor.execute("SELECT buyerid,password FROM buyer;")

        li = []
        for i in cursor:
            li.append(i)
        print(li)

        pwd = str(pwd)
        name = str(name)

        flag = 0
        for e, j in li:
            e = str(e)
            if e == name and j == pwd:
                flag = 1
                break

        if flag == 1:
            return render(request, 'general/search.html', {})
        else:
            return render(request, 'general/loginb.html', {})
    else:
        return render(request, 'general/loginb.html', {})


def logo(request):
    cursor = connection.cursor()

    if request.method == 'POST':
        name = request.POST.get('user')
        pwd = request.POST.get('pwd')

        cursor.execute("SELECT ownerid,password FROM owner;")

        li = []
        for i in cursor:
            li.append(i)
        print(li)

        pwd = str(pwd)
        name = str(name)

        flag = 0
        for e, j in li:
            e = str(e)
            if e == name and j == pwd:
                flag = 1
                break

        if flag == 1:

            cursor.execute("SELECT * FROM owner WHERE ownerid = " + name + ";")
            ld = []
            for j in cursor:
                ld.append(j)
            print(ld)

            cursor.execute(
                "SELECT propertyid, bhk, locality, city, state, features,agentid FROM property NATURAL JOIN owner WHERE owner.ownerid = " + name + ";")
            cards = []
            for x in cursor:
                cards.append(x)
            print(cards)
            context = {
                "ownerdata": ld,
                "propdata": cards,
            }

            return render(request, 'general/page2.html', context)
        else:
            return render(request, 'general/login.html', {})
    else:
        return render(request, 'general/login.html', {})


def agent(request):
    cursor = connection.cursor()

    #     context = {
    #         # "id":,
    #         # "name":,
    #         # "contact":,
    #         # "email":,
    #         # "completed":,
    #         # "rent":,
    #         # "sell":,
    #         # "rating":,
    #         # "net":,
    #     }

    return render(request, 'general/agent.html', {})


def search(request):
    if request.method == 'POST':

        size = request.POST.get('size')
        typ = request.POST.get('type')
        city = request.POST.get('city')
        budget = request.POST.get('budget')

        typ = str(typ)
        city = str(city)

        cursor = connection.cursor()
        print("select propertyid, type, bhk, category, locality, city, state, price, status from property where bhk <= " + size + " and type = '" +
              typ + "' and city ='" + city + "' and price <= " + budget + ";")
        cursor.execute("select propertyid, type, bhk, category, locality, city, state, price, status from property where bhk <= " + size + " and type = '" +
                       typ + "' and city ='" + city + "' and price <= " + budget + ";")

        cards = []
        for x in cursor:
            cards.append(x)
        print(cards)

        context = {
            "carddata": cards,
        }

        return render(request, 'general/search.html', context)
    else:
        return render(request, 'general/search.html', {})


def owner(request):

    # context = {
    #     "id":,
    #     "name":,
    #     "contact":,
    #     "email":,
    # }
    return render(request, 'general/page2.html', {})


def admin(request):
    querySet = Agent.objects.all()

    #agentid = 2
    #agentid = str(agentid)
    # cursor = connection.cursor()
    # cursor.execute("SELECT agentid FROM agent;")
    # prop = {
    #     "agentid": 102,
    #     ""
    # }

    q2 = Property.objects.filter(agentid=101)
    print(q2)

    context = {
        "object_list": querySet,
        "prop_list": q2,
    }
    print(context)
    return render(request, 'general/admin.html', context)

# def admin(request):
#     querySet = Agent.objects.all()

#     # agentid = 2
#     # agentid = str(agentid)
#     cursor = connection.cursor()
#     cursor.execute("SELECT agentid FROM agent;")

#     l = []
#     for i in cursor:
#         l.append(i)

#     context = {}
#     for i in l:
#         q2 = Property.objects.filter(agentid=i)
#         # print(q2)
#         context[i] = q2

#     context['object_list'] = querySet
#     print(context)
#     return render(request, 'general/admin.html', context)


def regis(request):
    if request.method == 'POST':

        name = request.POST.get('name')
        pwd = request.POST.get('pwd')
        email = request.POST.get('email')
        contact = request.POST.get('number')

        name = str(name)
        pwd = str(pwd)
        email = str(email)
        contact = str(contact)

        cursor = connection.cursor()

        print("select count(*) as count from buyer;")
        cursor.execute("select count(*) as count from buyer;")
        countSerial = []
        results = namedtuplefetchall(cursor)
        countSerial.append(results[0].count)
        print(countSerial)

        bid = countSerial[0] + 201
        bid = str(bid)

        cursor.execute("INSERT into buyer Values (" + bid + ", '" +
                       name + "', " + contact + ", '" + email + "', '" + pwd + "', NULL, NULL)")

        return render(request, 'general/search.html', {})
    else:
        return render(request, 'general/regis.html', {})
