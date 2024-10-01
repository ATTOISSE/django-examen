from rest_framework.routers import DefaultRouter
from .views import BookAPIView,UserAPIView,LoanAPIView
router = DefaultRouter()

router.register(r'books',BookAPIView,basename='books')
router.register(r'loans',LoanAPIView,basename='loans')
router.register(r'users',UserAPIView,basename='users')

urlpatterns = router.urls