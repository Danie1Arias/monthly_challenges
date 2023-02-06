from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

monthly_challenges = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for at least 20 min every day!",
    "march": "Learn Django for at least 20 minutes every day!",
    "april": "Learn Django for at least 20 minutes every day!",
    "may": "Walk for at least 20 min every day!",
    "june": "Walk for at least 20 min every day!",
    "july": "Walk for at least 20 min every day!",
    "august": "Walk for at least 20 min every day!",
    "october": "Walk for at least 20 min every day!",
    "november": "Walk for at least 20 min every day!",
    "december": "Walk for at least 20 min every day!"
}


def monthly_challenge_by_number(request, month):
    return HttpResponse(month)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month is not found")
