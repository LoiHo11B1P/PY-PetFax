from flask import ( Blueprint, render_template )
import json

pets = json.load(open('pets.json'))
print(pets)

bp = Blueprint('pet', __name__, url_prefix="/pets")

@bp.route('/')
def index(): 
    return render_template('/pets/index.html', pets=pets)

# for /pets/<index>
@bp.route('/<int:index>')
def showPage(index):

    petInfo = petDetail(index)

    return render_template('/pets/showPage.html', pet=petInfo)


def petDetail(index):

    for pet in pets:

        if pet['pet_id'] == index:

            return pet