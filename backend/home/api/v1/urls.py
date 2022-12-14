from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    ContactViewSet,
    CustomerTextViewSet,
    ForwordedMessageViewSet,
    HomePageViewSet,
    MessageViewSet,
    MessageActionViewSet,
    ProfileViewSet,
    ThreadViewSet,
    Thread_membersViewSet,
    ThreadActionViewSet,
    VerificationCodeViewSet,
)

from home.api.v1.viewsets import (
    SignupViewSet,
    LoginViewSet,
)

router = DefaultRouter()
router.register("signup", SignupViewSet, basename="signup")
router.register("login", LoginViewSet, basename="login")
router.register("verificationcode", VerificationCodeViewSet)
router.register("contact", ContactViewSet)
router.register("threadaction", ThreadActionViewSet)
router.register("thread", ThreadViewSet)
router.register("profile", ProfileViewSet)
router.register("thread_members", Thread_membersViewSet)
router.register("message", MessageViewSet)
router.register("homepage", HomePageViewSet)
router.register("messageaction", MessageActionViewSet)
router.register("customertext", CustomerTextViewSet)
router.register("forwordedmessage", ForwordedMessageViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
