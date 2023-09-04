from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm, UserChangeForm

def compte(request):
    conn_form = AuthenticationForm(data=request.POST or None)
    inscription_form = UserCreationForm(data=request.POST or None)

    if request.method == 'POST':
        if 'connexion' in request.POST:
            if conn_form.is_valid():
                user = conn_form.get_user()
                login(request, user)
                return redirect('ppm:dashboard')
        elif 'inscription' in request.POST:
            if inscription_form.is_valid():
                user = inscription_form.save()
                login(request, user)
                return redirect('ppm:dashboard')

    context = {
        'conn_form': conn_form,
        'inscription_form': inscription_form,
    }
    return render(request, 'compte/compte.html', context)

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm, UserCreationForm
from django.contrib.auth import update_session_auth_hash

@login_required
def modifier_compte(request):
    user_form = UserChangeForm(instance=request.user)
    password_form = PasswordChangeForm(request.user)

    if request.method == 'POST':
        if 'update_info' in request.POST:
            user_form = UserChangeForm(request.POST, instance=request.user)
            if user_form.is_valid():
                user_form.save()
                messages.success(request, 'Vos informations ont été mises à jour.')
                return redirect('compte:modifier_compte')

        if 'change_password' in request.POST:
            password_form = PasswordChangeForm(request.user, request.POST)
            if password_form.is_valid():
                user = password_form.save()
                update_session_auth_hash(request, user)
                messages.success(request, 'Votre mot de passe a été changé avec succès.')
                return redirect('compte:modifier_compte')

    context = {
        'user_form': user_form,
        'password_form': password_form,
    }
    return render(request, 'compte/modifier_compte.html', context)

@login_required
def ajouter_utilisateur(request):
    if request.method == 'POST':
        new_username = request.POST['new_username']
        new_password = request.POST['new_password']

        # Vous devriez utiliser un moyen sécurisé pour stocker le mot de passe, par exemple en utilisant bcrypt.
        # Pour cet exemple, nous utilisons UserCreationForm, mais en pratique, une gestion plus sécurisée est recommandée.
        new_user = UserCreationForm({'username': new_username, 'password1': new_password, 'password2': new_password})

        if new_user.is_valid():
            new_user.save()
            messages.success(request, 'Nouvel utilisateur ajouté avec succès.')
            return redirect('compte:modifier_compte')
        else:
            messages.error(request, 'Erreur lors de l\'ajout du nouvel utilisateur.')

    return redirect('compte:modifier_compte')  # Redirection en cas de requête GET
