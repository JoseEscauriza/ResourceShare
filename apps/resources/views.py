from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.db.models import Count
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .form import PostResourceForm
from .models import Resources, Tag
from apps.user.models import User
from .utils import generate_cat_count_list


# def home_page(request):
#     cnt = Resources.objects.all().count()
#     user_cnt = User.objects.filter(is_active=True).count()
#     res_per_cat = Resources.objects.values(
#         "cat_id__cat").annotate(cnt=Count("cat_id"))

#     context = {
#         "cnt": cnt,
#         "user_cnt": user_cnt,
#         "res_per_cat": res_per_cat,
#     }
#     return render(
#         request=request,
#         template_name="resources/home.html",
#         context=context,
#     )


# def home_page_old(request):
#     cnt = Resources.objects.all().count()
#     active_users = User.objects.filter(is_active=True).count()
#     resource_per_cat = Resources.objects.values(
#         'cat_id__cat').annotate(cnt=Count('cat_id'))
#     response = f"""
#     <html><h1>Welcome to ResourceShare</h1></html>
#     <p> {cnt} resources and counting!</p>
#     <p> {active_users} users and counting </p>

#     <h3>Resources per category</h3>
#     <ul>
#         {generate_cat_count_list(resource_per_cat)}
#     </ul>
#     """
#     return HttpResponse(response)


@login_required
def resource_detail(request, id):
    max_viewed_resources = 5

    viewed_resources = request.session.get('viewed_resources', [])

    res = (
        Resources.objects.select_related("user_id", "cat_id")
        .prefetch_related("tags")
        .get(pk=id)
    )

    # prepare data
    viewed_resource = [id, res.title]

    # check if that data exists already and remove it
    if viewed_resource in viewed_resources:
        viewed_resources.remove(viewed_resource)

    # add it to our list in first position
    viewed_resources.insert(0, viewed_resource)

    # limit our list
    viewed_resources = viewed_resources[:max_viewed_resources]

    # add it back to the session
    request.session['viewed_resources'] = viewed_resources

    response = f"""
        <html>
        <h1> {res.title}</h1>
        <p><b>Posted by:</b> {res.user_id}</p>
        <p><b>Link:</b> {res.link}</p>
        <p><b>Description:</b> {res.description}</p>
        <p><b>Category:</b> {res.cat_id}</p>
        <p><b>Tags:</b> {res.all_tags()}</p>
        </html>
    """
    return HttpResponse(response)


@login_required
def resource_post(request):
    if request.method == 'GET':
        # Unbound
        form = PostResourceForm()
        return render(
            request,
            "resources/resource_post.html",
            {'form': form},
        )
    else:
        # Bound
        form = PostResourceForm(request.POST)

        # validation

        if form.is_valid():
            data = form.cleaned_data
            # ADD USER ID
            data['user_id_id'] = 1
            # SAVE TO DB
            Resources.objects.create(
                description=data['description'],
                link=data['link'],
                user_id_id=data['user_id_id'],
                title=data['title'],
            )
            # REDIRECT TO HOME PAGE
            return redirect(home_page)


class HomePage(TemplateView):

    def get(self, request):
        cnt = Resources.objects.all().count()
        user_cnt = User.objects.filter(is_active=True).count()
        res_per_cat = Resources.objects.values(
            "cat_id__cat").annotate(cnt=Count("cat_id"))

        context = {
            "cnt": cnt,
            "user_cnt": user_cnt,
            "res_per_cat": res_per_cat,
        }
        return render(
            request=request,
            template_name="resources/home.html",
            context=context,
        )
