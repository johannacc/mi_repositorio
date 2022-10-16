from django.http import HttpResponse
from django.template import loader
from datetime import datetime
from member.models import Family




def create_member(request, name: str, last_name: str, age: int, birth_date : int):


    template = loader.get_template("template_member.html")
    birth_date = datetime.strptime (birth_date, "%m"-"%d"-"%Y")


    member =Family(
        name=name, last_name=last_name, age=age, birth_date=birth_date)
    member.save()  # save into the DB

    context_dict = {"member": member}
    render = template.render(context_dict)
    return HttpResponse(render)
