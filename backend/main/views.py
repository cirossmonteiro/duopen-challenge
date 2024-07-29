import requests
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from main.models import Account, Item, Transaction, User
from main.serializers import AccountSerializer, ItemSerializer, TransactionSerializer, UserSerializer

def retrieve_by_itemid(item_id):
    # to-do: iterate over pages
    url_apikey = "https://api.pluggy.ai/auth"
    payload_apikey = {
        "clientId": "76485c65-4541-4fef-9124-0c0f6a3da8e8",
        "clientSecret": "7249a568-bf7a-450e-af59-8415049bed9d"
    }
    response_apikey = requests.post(url_apikey, json=payload_apikey)
    headers = {
        "accept": "application/json",
        "X-API-KEY": response_apikey.json()["apiKey"]
    }

    # fetch item
    url_items = f"https://api.pluggy.ai/items/{item_id}"
    response_items = requests.get(url_items, headers=headers)
    item = Item.objects.create(
        id=item_id,
        createdAt=response_items.json()["createdAt"],
        updatedAt=response_items.json()["updatedAt"],
    )

    # fetch accounts
    url_accounts = f"https://api.pluggy.ai/accounts?itemId={item_id}"
    response_accounts = requests.get(url_accounts, headers=headers)

    for account_data in response_accounts.json()["results"]:
        print(28, account_data["id"])
        accountId = account_data["id"]
        account = Account.objects.create(
            id=accountId, item=item,
            createdAt=account_data["createdAt"],
            updatedAt=account_data["updatedAt"],
        )

        # fetch transactions
        url_transactions = f"https://api.pluggy.ai/transactions?accountId={accountId}"
        response_transactions = requests.get(url_transactions, headers=headers)

        for transaction_data in response_transactions.json()["results"]:
            transactionId = transaction_data["id"]
            transaction = Transaction.objects.create(
                id=transactionId, account=account,
                createdAt=transaction_data["createdAt"],
                updatedAt=transaction_data["updatedAt"],
            )
        print(35, response_transactions.json()["total"])

    return True

class AccountViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class ItemViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    @action(methods=['post'], detail=True)
    def fetch(self, request, pk=None):
        print(12, "here", pk)
        return Response(retrieve_by_itemid(pk))
    
class TransactionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
