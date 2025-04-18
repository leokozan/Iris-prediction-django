from django.views import View
from django.shortcuts import render
from app_iris.models import IrisModel
from app_iris.validations import IrisValidations
import traceback

class IrisListView(View):
    def get(self, request):
        context = {
            'data_set': IrisModel.objects.all()
        }
        return render(request, 'app_iris/list.html', context=context)

class IrisCreateView(View):
    def get(self, request):
        return render(request, 'app_iris/create.html')
    
    def post(self, request):
        try:
            iris = IrisValidations()
            iris.set_sepal_length(float(request.POST.get('sepal_length')[0]))
            iris.set_sepal_width(float(request.POST.get('sepal_width')[0]))
            iris.set_petal_length(float(request.POST.get('petal_length')[0]))
            iris.set_petal_width(float(request.POST.get('petal_width')[0]))
            iris.set_specie(request.POST.get('specie'))

            model = iris.to_model()
            model.save()
        except:
            # tratativa de erro
            traceback.print_exc()
        
        return render(request, 'app_iris/create.html')
    
class IrisUpdateView(View):
    def get(self, request, id):
        context = {
            'data': IrisModel.objects.get(id=int(id)), # SELECT * FROM IRIS WHERE ID=?;
            'species': ['setosa', 'versicolor', 'virginica']
        }
        return render(request, 'app_iris/update.html', context)
    
    def post(self, request, id):
        # implementar aqui
        ...

class IrisDashboardView(View):
    def get(self, request):
        context = {
            'setosa': 5, 
            'versicolor': 6, 
            'virginica': 4
        }
        return render(request, 'app_iris/dashboard.html', context)