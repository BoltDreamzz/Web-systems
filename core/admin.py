from django.contrib import admin
# from import_export.admin import ImportExportModelAdmin

from .models import Category, Technology, Project, TeamMember, Testimonial, Comment


# class ProjectAdmin(ImportExportModelAdmin):
#     search_fields = ["user__username", "name"]
#     list_filter = ["title", "category"]
#     list_editable = ["client"]
#     list_display = ["title", "start_date", "client", "champion", "category", "views"]
#     list_per_page = 100
#     # prepopulated_fields = {"slug": ("name", )}


admin.site.register(Category)
admin.site.register(Technology)
admin.site.register(Project)
admin.site.register(TeamMember)
admin.site.register(Testimonial)
admin.site.register(Comment)
