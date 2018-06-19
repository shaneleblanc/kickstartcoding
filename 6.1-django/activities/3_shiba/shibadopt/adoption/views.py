from django.shortcuts import render

shibas = [
    {
        'image_src': 'https://i.imgur.com/VEslUBl.png',
        'name': 'Tacopup',
        'age': 2,
        'id_number': 1,
    },
    {
        'image_src': 'https://i.imgur.com/iCCNZZF.jpg',
        'name': 'Pupperwave',
        'age': 3,
        'id_number': 2,
    },
    {
        'image_src': 'https://i.imgur.com/XiznnoN.jpg',
        'name': 'Wow-Banana',
        'age': 5,
        'id_number': 3,
    },
    {
        'image_src': 'https://i.imgur.com/ORizDRq.png',
        'name': 'Galaxy-Doggo',
        'age': 2,
        'id_number': 4,
    },
    {
        'image_src': 'https://i.imgur.com/APMdtxs.png',
        'name': 'Sweetdoggo',
        'age': 4,
        'id_number': 5,
    },
]

def homepage(request):
    context = {
        'shiba_count': len(shibas),
        'all_shibas': shibas,
    }
    return render(request, 'homepage.html', context)

def add_a_shiba(request):
    

def adopt_a_shiba(request):
    context = {
        'shiba_count': len(shibas),
        'all_shibas': shibas,
    }
    if 'number' in request.GET:
        number = int(request.GET['number'])
        print('They entered:', number)

        for shiba in shibas:
            if shiba['id_number'] == number:
                print('found shiba, removing!')
                context['was_adopted'] = shiba
                shibas.remove(shiba)

        if 'redirect' in request.POST:
            return redirect('/')
    return render(request, 'adoption.html', context)

def add_a_shiba(request):
    context = {}
    return render(request, 'adoption.html', context)
