from api.models import Purchase


def purchase_counter(request):
    if request.user.is_authenticated:
        purchase_counter = Purchase.objects.filter(user=request.user).count()
        return {'purchase_counter': purchase_counter}
    return {'purchase_counter': 0}
