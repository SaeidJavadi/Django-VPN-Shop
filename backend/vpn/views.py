from django.shortcuts import render,  redirect
from django.contrib.auth.decorators import login_required
from vpn.models import vpnlist, Help, Order
from django.views.generic import ListView, DetailView
from vpn.forms import ContactForm
from django.contrib import messages
from django.utils.translation import gettext_lazy as _


def home(request):
    vpli = vpnlist.objects.all().order_by('row')
    return render(request=request, template_name="vpn/home.html", context={'vpnall': vpli})


def vpnbuy(request):
    """
        Handle VPN purchase form submission.

        This view processes the POST request sent from the VPN purchase page.
        Currently, it only retrieves the selected VPN ID and redirects the user
        to the home page.

        ⚠️ IMPORTANT (Production Notice):
        The payment logic is intentionally NOT implemented here.
        In a production environment, this section must be completed by:
        - Integrating a real payment gateway (e.g., Stripe, Zarinpal, PayPal)
        - Validating the selected VPN ID
        - Creating an order/payment record in the database
        - Handling payment success and failure callbacks securely

        This placeholder implementation exists for demonstration
        and testing purposes only.
    """
    if request.method == "POST":
        vpnid = request.POST.get('vvpnid')
        # return redirect('payment:pay', vid=vpnid)
        # return redirect('https://zarinp.al/ilmabeauty')
        vpn = vpnlist.objects.get(id=vpnid)
        Order.objects.create(user=request.user, vpn=vpn)
        return redirect('vpn:dashboard')
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
            messages.success(request, _(
                'Your message has been successfully sent'), extra_tags='alert alert-success')
            return redirect('vpn:contact')
        else:
            messages.success(request, _('An error occurred while sending your message'),
                             extra_tags='alert alert-warning')
    else:
        form = ContactForm()
    return render(request, template_name='vpn/contact.html', context={'form': form})


@login_required()
def dashboard(request):
    ordrs = Order.objects.filter(user=request.user)
    return render(request, "vpn/dashboard.html", {'ordrs': ordrs})


def handler404(request, *args, **argv):
    return render(request, 'vpn/404.html')


def handler500(request, *args, **argv):
    return render(request, 'vpn/500.html')
