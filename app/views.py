from django.shortcuts import render, redirect
from .models import Note, NoteBook
# Create your views here.

def notebook(request, notebook_id):
	notebook_object = NoteBook.objects.get(id=notebook_id)
	
	context = {
		'list': notebook_object.note_set.all(),
		'notebook_id': notebook_id,
	}
	return render(request, 'notebook.html', context)


def note_edit(request, note_id):
	context = {
		'object': Note.objects.get(id=note_id)
	}
	return render(request, 'note.html', context)


def note_detail(request, note_id):
	context = {
		'object': Note.objects.get(id=note_id),
	}
	return render(request, 'note_detail.html', context)

def save_note(request, note_id):
	title = request.POST.get("title")
	body = request.POST.get("body")

	note = Note.objects.get(id=note_id)
	note.title = title
	note.body = body
	note.save()
	
	return redirect("/detail/"+str(note_id))

def create(request, notebook_id):
	context = {
		'notebook_id': notebook_id
	}
	return render(request, 'create.html', context)

def submit_note(request, notebook_id):
	Note.objects.create(
		title=request.POST.get("title"),
		body=request.POST.get("body"),
		notebook=NoteBook.objects.get(id=notebook_id)
		)

	return redirect('/notebook/%s/'%notebook_id)


def delete(request, z):
	y = Note.objects.get(id=z)
	y.delete()
	x = y.notebook
	return redirect('/notebook/%s/'% x.id)


#this home page shows the list of notebooks
def home(request):
	context = {
		'notebooklist': NoteBook.objects.all()
	}
	return render(request, 'home.html', context)

def createnotebook(request):
	return render(request, 'createnotebook.html', {})

def save_notebook(request, notebook_id):
	title = request.POST.get("title")
	notebook = NoteBook.objects.get(id=notebook_id)
	notebook.title = title
	notebook.save()


def submit_notebook(request):
	NoteBook.objects.create(title=request.POST.get("title"))

	return redirect('/home/')
