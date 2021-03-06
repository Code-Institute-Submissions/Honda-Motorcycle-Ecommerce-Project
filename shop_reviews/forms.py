from django import forms
from .models import ShopReview


class ShopReviewForm(forms.ModelForm):
    class Meta:
        model = ShopReview
        fields = ('review_title', 'reviewer_name', 'review_description')
