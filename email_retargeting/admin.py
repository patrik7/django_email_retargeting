from django.contrib import admin
from django.urls import reverse

from email_retargeting.models import Campaign, Email, EmailTemplate


def make_live(modeladmin, request, queryset):
	queryset.update(live=True)
make_live.short_description = "Set selected campaigns as live"


class CampaignAdmin(admin.ModelAdmin):
	list_display = ['name', 'template', 'live']
	actions = [make_live]
	pass


class EmailTemplateAdmin(admin.ModelAdmin):
	list_display = ['name', 'subject']
	pass


class EmailAdmin(admin.ModelAdmin):
	list_display = ['to_email', 'campaign', 'send_explain', 'sent_at', 'failed', 'resend']
	search_fields = ['to_email']

	def failed(self, email):
		return 'Failed' if len(email.failure) > 0 else ''
	failed.short_description = 'Failed'

	def resend(self, email):
		return '<a href="%s">Resend</a>' % reverse("admin_email_resend", kwargs={'email_id': email.id})
	resend.short_description = 'Resend email'
	resend.allow_tags = True


admin.site.register(Campaign, CampaignAdmin)
admin.site.register(EmailTemplate, EmailTemplateAdmin)
admin.site.register(Email, EmailAdmin)
