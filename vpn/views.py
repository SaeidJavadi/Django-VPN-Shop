from django.shortcuts import render,  redirect
from django.contrib.auth.decorators import login_required
from vpn.models import vpnlist, Help
from django.views.generic import ListView, DetailView
from vpn.forms import ContactForm
from django.contrib import messages
from django.utils.translation import gettext_lazy as _

def home(request):
    vpli = vpnlist.objects.all().order_by('row')
    return render(request=request, template_name="vpn/home.html", context={'vpnall': vpli})


def vpnbuy(request):
    if request.method == "POST":
        vpnid = request.POST.get('vvpnid')
        # return redirect('payment:pay', vid=vpnid)
        return redirect('https://zarinp.al/ilmabeauty')
    else:
        vpli = vpnlist.objects.all().order_by('row')
        return render(request=request, template_name="vpn/buy.html", context={'vpnall': vpli})


@login_required()
def buyVerify(request):
    v = vpnlist.objects.get(id=request.POST.get('vpnid'))
    return render(request=request, template_name="vpn/verify.html", context={'vpn': v})


class HelpListView(ListView):
    model = Help


class HelpDetailView(DetailView):
    model = Help

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, _('Your message has been successfully sent'), extra_tags='alert alert-success')
            return redirect('base:contact')
        else:
            messages.success(request, _('An error occurred while sending your message'),
                             extra_tags='alert alert-warning')
    else:
        form = ContactForm()
    return render(request, template_name='vpn/contact.html', context={'form': form})
