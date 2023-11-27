from django.contrib import admin
from dm_portfolio.models import(
        UserProfile,
        Testimonial,
        Media,
        Portfolio,
        Blog,
        Certificate,
        Skill
)

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')
    list_filter = ('user',)
    search_fields = ('id', 'user', 'is_active', 'created_at', 'updated_at')
    ordering = ('id', 'user')

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_active')
    list_filter = ('id', 'name', 'is_active')
    search_fields = ('id', 'name', 'is_active')
    ordering = ('id', 'name', 'is_active')

@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image')
    list_filter = ('id', 'name', 'image')
    search_fields = ('id', 'name', 'image')
    ordering = ('id', 'name', 'image')

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image', 'is_active')
    list_filter = ('id', 'name', 'image', 'is_active')
    search_fields = ('id', 'name', 'image', 'is_active')
    ordering = ('id', 'name', 'image', 'is_active')
    readonly_fields = ('slug',)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image')
    list_filter = ('id', 'name', 'image')
    search_fields = ('id', 'name', 'image')
    ordering = ('id', 'name', 'image')
    readonly_fields = ('slug',)

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_active')
    list_filter = ('id', 'name',  'is_active')
    search_fields = ('id', 'name', 'is_active')
    ordering = ('id', 'name', 'is_active')

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'score')
    list_filter = ('id', 'name', 'score')
    search_fields = ('id', 'name', 'score')
    ordering = ('id', 'name', 'score')