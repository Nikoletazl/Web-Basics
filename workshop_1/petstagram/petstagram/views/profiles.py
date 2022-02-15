from django.shortcuts import redirect, render

from petstagram.main.forms import CreateProfileForm, EditProfileForm, DeleteProfileForm
from petstagram.main.models import Pet, PetPhoto, Profile

from petstagram.main.helpers import get_profile


def show_profile(request):
    profile = get_profile()
    if not profile:
        return redirect('401_error.html')
    pets = Pet.objects.filter(user_profile=profile)
    pet_photos = PetPhoto.objects.filter(tagged_pets__in=pets).distinct()

    total_likes_count = sum(pp.likes for pp in pet_photos)
    total_images_count = len(pet_photos)
    context = {
        'profile': get_profile(),
        'total_likes_count': total_likes_count,
        'total_images_count': total_images_count,
        'pets': pets,
    }
    return render(request, 'profile_details.html', context)


def profile_action(request, form_class, success_url, instance, template_name):
    if request.method == 'POST':
        form = form_class(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect(success_url)
    else:
        form = form_class(instance=instance)

    context = {
        'form': form,
    }

    return render(request, template_name, context)


def create_profile(request):
    return profile_action(request, CreateProfileForm, 'index', Profile(), 'profile_create.html')


def edit_profile(request):
    return profile_action(request, EditProfileForm, 'profile details', get_profile(), 'profile_edit.html')


def delete_profile(request):
    return profile_action(request, DeleteProfileForm, 'index', get_profile(), 'profile_delete.html')
