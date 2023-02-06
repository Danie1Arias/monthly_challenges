from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


def monthly_challenge(request, month):
    match month:
        case "january":
            challenge_text = "Eat no meat for the entire month!"
        case "february":
            challenge_text = "Walk for at least 20 min every day!"
        case "march":
            challenge_text = "Learn Django for at least 20 minutes every day!"
        case _:
            return HttpResponseNotFound("This month is not supported!")

    return HttpResponse(challenge_text)
