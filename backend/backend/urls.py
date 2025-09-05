from django.contrib import admin
from django.urls import path, include
from backendApp import views 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # AUTENTICAÇÃO ------------------------------------------------------------------------------------
    path('api/auth/login/', views.login, name='login'),
    path('api/auth/logout/', views.logout, name='logout'),
    path('api/auth/pessoal/', views.verifica_autenticacao, name='verifica_autenticacao'),
    path('api/estatisticas/', views.estatisticas, name='estatisticas'),

    # UTILIZADORES ------------------------------------------------------------------------------------
    path('api/utilizadores/', views.utilizadores, name='utilizadores'),
    path('api/utilizadores/<int:id>/', views.utilizador, name='utilizador'),
    path('api/utilizadores/disponiveis/', views.utilizadores_disponiveis, name='utilizadores_disponiveis'),
    path('api/staff/', views.staff, name='staff'),
    
    path('api/utilizadores/<int:id>/perfil/', views.altera_perfil, name='altera_perfil'),
    path('api/utilizadores/<int:id>/password/', views.altera_password, name='altera_password'),
    path('api/utilizadores/<int:id>/estado/', views.altera_estado, name='altera_estado'),

    # JOGADORES ------------------------------------------------------------------------------------
    path('api/jogadores/', views.jogadores, name='jogadores'), 
    path('api/jogadores/<int:id>/', views.jogador, name='jogador'), 
    
    # JOGADORES --> INSCRIÇÕES ------------------------------------------------------------------------------------    
    path('api/jogadores/<int:id>/inscricoes/', views.inscricoes_jogador, name='inscricoes_jogador'),
    path('api/jogadores/<int:id>/inscricoes/documentos/', views.upload_documentos, name='upload_documentos'),

    # MODALIDADES ------------------------------------------------------------------------------------
    path('api/modalidades/', views.modalidades, name='modalidades'), 
    path('api/modalidades/<int:id>/', views.modalidade, name='modalidade'),
    
    # MODALIDADES --> ÉPOCAS ------------------------------------------------------------------------------------
    path('api/modalidades/<int:id>/epocas/', views.epocas, name='epocas'),
    path('api/epocas/<int:id>/', views.epoca, name='epoca'),

    # MODALIDADES --> EQUIPAS ------------------------------------------------------------------------------------
    path('api/modalidades/<int:id>/equipas/', views.equipas, name='equipas'),
    path('api/equipas/<int:id>/', views.equipa, name='equipa'),

    # EQUIPAS --> PLANTEL ------------------------------------------------------------------------------------
    path('api/equipas/<int:id>/elementos-disponiveis/', views.elementos_disponiveis, name='elementos_disponiveis'),
    path('api/equipas/<int:id>/elementos/', views.associa_elemento, name='associa_elemento'),

    # EQUIPAS --> JOGOS ------------------------------------------------------------------------------------
    path('api/equipas/<int:id>/jogos/', views.jogos, name='jogos'),
    path('api/jogos/<int:id>/', views.jogo, name='jogo'),
    path('api/jogos/', views.jogos_clube, name='jogos_clube'),

    # EQUIPAS --> COMPETIÇÕES ------------------------------------------------------------------------------------
    path('api/equipas/<int:id>/competicoes/', views.competicoes, name='competicoes'),
    path('api/competicoes/<int:id>/', views.competicao, name='competicao'),

    # SÓCIOS ------------------------------------------------------------------------------------
    path('api/socios/', views.socios, name='socios'),

    # SÓCIOS --> CATEGORIAS ------------------------------------------------------------------------------------
    path('api/categorias/', views.categorias, name='categorias'),
    path('api/categorias/<int:id>/', views.categoria, name='categoria'),
    path('api/categorias/<int:id>/estado/', views.estado_categoria, name='estado_categoria'),
    path('api/categorias/historico/', views.historico_categorias, name='historico_categorias'),

    # QUOTAS ------------------------------------------------------------------------------------
    path('api/quotas/', views.quotas, name='quotas'),
    path('api/quotas/<int:id>/registo/', views.regista_pagamento_quotas, name='regista_pagamento_quotas'),
 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
