# library/views.py
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Book, User, Transaction
from .serializers import BookSerializer, UserSerializer, TransactionSerializer
from rest_framework.decorators import action
from django.utils import timezone

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    # إضافة نقطة النهاية لعرض الكتب المتاحة فقط
    @action(detail=False, methods=['get'])
    def available_books(self, request):
        available_books = Book.objects.filter(number_of_copies__gt=0)
        serializer = BookSerializer(available_books, many=True)
        return Response(serializer.data)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]

    # إضافة نقطة النهاية للاستعارة
    @action(detail=False, methods=['post'])
    def checkout(self, request):
        book_id = request.data.get('book_id')
        user = request.user

        try:
            book = Book.objects.get(id=book_id)
        except Book.DoesNotExist:
            return Response({"error": "Book not found"}, status=status.HTTP_404_NOT_FOUND)

        if book.number_of_copies < 1:
            return Response({"error": "No available copies of this book"}, status=status.HTTP_400_BAD_REQUEST)

        # تخفيض عدد النسخ المتاحة
        book.number_of_copies -= 1
        book.save()

        # إنشاء سجل معاملة جديدة
        transaction = Transaction.objects.create(user=user, book=book)
        return Response(TransactionSerializer(transaction).data, status=status.HTTP_201_CREATED)

    # إضافة نقطة النهاية للإرجاع
    @action(detail=False, methods=['post'])
    def return_book(self, request):
        transaction_id = request.data.get('transaction_id')
        try:
            transaction = Transaction.objects.get(id=transaction_id, user=request.user, returned_date=None)
        except Transaction.DoesNotExist:
            return Response({"error": "Transaction not found or book already returned"}, status=status.HTTP_404_NOT_FOUND)

        # تحديث تاريخ العودة وزيادة النسخ المتاحة
        transaction.returned_date = timezone.now()
        transaction.save()

        book = transaction.book
        book.number_of_copies += 1
        book.save()

        return Response(TransactionSerializer(transaction).data, status=status.HTTP_200_OK)
