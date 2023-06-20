from gameblock.models import Player


def user_extended_context_processor(request):
    is_player = Player.objects.filter(user_id__id=request.user.id).exists()

    return {
        'is_player': is_player,
    }