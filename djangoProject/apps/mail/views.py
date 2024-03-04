from django.http import HttpResponse
import json
from drf_yasg.utils import swagger_auto_schema
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from rest_framework.decorators import api_view
from djangoProject.apps.mail.docs import *
from djangoProject.apps.mail.models import Letter, Parcel
from djangoProject.apps.mail.functions import get_variable, id_is_valid
from djangoProject.apps.mail.serializers import LetterSerializer, ParcelSerializer
from django.conf import settings


DEBUG = settings.DEBUG


@swagger_auto_schema(method='GET', operation_summary="Получить список всех объектов на почте.",
                     manual_parameters=[object_param],
                     responses=get_objects_responses)
@api_view(["GET"])
def get_objects(request):
    try:
        object_type = get_variable('object', request)
        objects_dict = {'letters': [], 'parcels': []}
        order_type = get_variable('order_type', request)
        if order_type in ['ASC', 'DESC', 'asc', 'desc']:
            order_type = order_type.lower()
        else:
            order_type = None
        order_field = get_variable('order_field', request)
        if order_field not in ['sender', 'receiver', 'weight', 'amount']:
            order_field = None
        sender = get_variable('sender', request)
        receiver = get_variable('receiver', request)
        index_dispatch = get_variable('index_dispatch', request)
        index_receipt = get_variable('index_receipt', request)
        is_given = get_variable('is_given', request)
        if is_given == '0':
            is_given = False
        elif is_given == '1':
            is_given = True
        else:
            is_given = None
        if object_type == '0':
            letters = Letter.objects.all()

            # Фильтрация
            if sender:
                letters = letters.filter(sender=sender)
            if receiver:
                letters = letters.filter(receiver=receiver)
            if index_dispatch:
                letters = letters.filter(index_dispatch=index_dispatch)
            if index_receipt:
                letters = letters.filter(index_receipt=index_receipt)
            if is_given:
                letters = letters.filter(is_given=is_given)

            # Сортировка
            if order_type and order_field in ['sender', 'receiver', 'weight']:
                if order_type == 'asc':
                    order = f'-{order_field}'
                else:
                    order = f'{order_field}'
                letters = letters.order_by(order)

            letters = letters.values(
                'id',
                'sender',
                'receiver',
                'point_of_dispatch',
                'point_of_receipt',
                'index_dispatch',
                'index_receipt',
                'letter_type',
                'weight',
                'is_given'
            )

            for letter in letters:
                objects_dict['letters'].append({
                    'id': letter['id'],
                    'sender': letter['sender'],
                    'receiver': letter['receiver'],
                    'point_of_dispatch': letter['point_of_dispatch'],
                    'point_of_receipt': letter['point_of_receipt'],
                    'index_dispatch': letter['index_dispatch'],
                    'index_receipt': letter['index_receipt'],
                    'letter_type': letter['letter_type'],
                    'weight': letter['weight'],
                    'is_given': letter['is_given'],
                })
        elif object_type == 1:
            parcels = Parcel.objects.all()

            # Фильтрация
            if sender:
                parcels = parcels.filter(sender=sender)
            if receiver:
                parcels = parcels.filter(receiver=receiver)
            if index_dispatch:
                parcels = parcels.filter(index_dispatch=index_dispatch)
            if index_receipt:
                parcels = parcels.filter(index_receipt=index_receipt)
            if is_given:
                parcels = parcels.filter(is_given=is_given)

            # Сортировка
            if order_type and order_field in ['sender', 'receiver', 'weight']:
                if order_type == 'asc':
                    order = f'-{order_field}'
                else:
                    order = f'{order_field}'
                parcels = parcels.order_by(order)

            parcels = parcels.values(
                'id',
                'sender',
                'receiver',
                'point_of_dispatch',
                'point_of_receipt',
                'index_dispatch',
                'index_receipt',
                'parcel_type',
                'amount',
                'phone',
                'is_given'
            )
            for parcel in parcels:
                objects_dict['parcels'].append({
                    'id': parcel['id'],
                    'sender': parcel['sender'],
                    'receiver': parcel['receiver'],
                    'point_of_dispatch': parcel['point_of_dispatch'],
                    'point_of_receipt': parcel['point_of_receipt'],
                    'index_dispatch': parcel['index_dispatch'],
                    'index_receipt': parcel['index_receipt'],
                    'parcel_type': parcel['parcel_type'],
                    'amount': parcel['amount'],
                    'phone': parcel['phone'],
                    'is_given': parcel['is_given'],
                })
        else:
            letters = Letter.objects.all()

            # Фильтрация
            if sender:
                letters = letters.filter(sender=sender)
            if receiver:
                letters = letters.filter(receiver=receiver)
            if index_dispatch:
                letters = letters.filter(index_dispatch=index_dispatch)
            if index_receipt:
                letters = letters.filter(index_receipt=index_receipt)
            if is_given:
                letters = letters.filter(is_given=is_given)

            # Сортировка
            if order_type and order_field in ['sender', 'receiver', 'weight']:
                if order_type == 'asc':
                    order = f'-{order_field}'
                else:
                    order = f'{order_field}'
                letters = letters.order_by(order)

            letters = letters.values(
                'id',
                'sender',
                'receiver',
                'point_of_dispatch',
                'point_of_receipt',
                'index_dispatch',
                'index_receipt',
                'letter_type',
                'weight',
                'is_given'
            )
            for letter in letters:
                objects_dict['letters'].append({
                    'id': letter['id'],
                    'sender': letter['sender'],
                    'receiver': letter['receiver'],
                    'point_of_dispatch': letter['point_of_dispatch'],
                    'point_of_receipt': letter['point_of_receipt'],
                    'index_dispatch': letter['index_dispatch'],
                    'index_receipt': letter['index_receipt'],
                    'letter_type': letter['letter_type'],
                    'weight': letter['weight'],
                    'is_given': letter['is_given'],
                })
            parcels = Parcel.objects.all()

            # Фильтрация
            if sender:
                parcels = parcels.filter(sender=sender)
            if receiver:
                parcels = parcels.filter(receiver=receiver)
            if index_dispatch:
                parcels = parcels.filter(index_dispatch=index_dispatch)
            if index_receipt:
                parcels = parcels.filter(index_receipt=index_receipt)
            if is_given:
                parcels = parcels.filter(is_given=is_given)

            # Сортировка
            if order_type and order_field in ['sender', 'receiver', 'weight']:
                if order_type == 'asc':
                    order = f'-{order_field}'
                else:
                    order = f'{order_field}'
                parcels = parcels.order_by(order)
            parcels = parcels.values(
                'id',
                'sender',
                'receiver',
                'point_of_dispatch',
                'point_of_receipt',
                'index_dispatch',
                'index_receipt',
                'parcel_type',
                'amount',
                'phone',
                'is_given'
            )
            for parcel in parcels:
                objects_dict['parcels'].append({
                    'id': parcel['id'],
                    'sender': parcel['sender'],
                    'receiver': parcel['receiver'],
                    'point_of_dispatch': parcel['point_of_dispatch'],
                    'point_of_receipt': parcel['point_of_receipt'],
                    'index_dispatch': parcel['index_dispatch'],
                    'index_receipt': parcel['index_receipt'],
                    'parcel_type': parcel['parcel_type'],
                    'amount': parcel['amount'],
                    'phone': parcel['phone'],
                    'is_given': parcel['is_given'],
                })
        return HttpResponse(json.dumps(objects_dict, ensure_ascii=False), status=200)
    except Exception as e:
        error = str(e) if DEBUG else ""
        return HttpResponse(
            json.dumps(
                {'state': 'error', 'message': f'Произошла непредвиденная ошибка.',
                 'details': {'error': error},
                 'instance': request.path}, ensure_ascii=False), status=404)


@swagger_auto_schema(method='POST', operation_summary="Создать объект.",
                     responses=create_object_responses,
                     request_body=create_object_request_body)
@api_view(["POST"])
def create_object(request):
    try:
        if request.body:
            request_body = json.loads(request.body)
        else:
            return HttpResponse(json.dumps(
                {'state': 'error', 'message': 'Body запроса пустое.', 'details': {}, 'instance': request.path},
                ensure_ascii=False), status=400)
        object_type = request_body['object']
        if object_type == 0:
            data = {
                'sender': request_body['sender'],
                'receiver': request_body['receiver'],
                'point_of_dispatch': request_body['point_of_dispatch'],
                'point_of_receipt': request_body['point_of_receipt'],
                'index_dispatch': request_body['index_dispatch'],
                'index_receipt': request_body['index_receipt'],
                'letter_type': request_body['letter_type'],
                'weight': request_body['weight'],
            }
            letter = LetterSerializer(data=data)
            if letter.is_valid():
                letter.create(data)
            else:
                errors = letter.errors
                errors_list = []
                for error in errors:
                    field = error
                    text = errors[error][0].title()
                    errors_list.append(f'Некорректно указаны данные в поле {field}. {text}')
                return HttpResponse(
                    json.dumps(
                        {'state': 'error', 'message': f'Некорректно указаны данные.',
                         'details': {'errors': errors_list},
                         'instance': request.path}, ensure_ascii=False), status=404)
        elif object_type == 1:
            data = {
                'sender': request_body['sender'],
                'receiver': request_body['receiver'],
                'point_of_dispatch': request_body['point_of_dispatch'],
                'point_of_receipt': request_body['point_of_receipt'],
                'index_dispatch': request_body['index_dispatch'],
                'index_receipt': request_body['index_receipt'],
                'parcel_type': request_body['parcel_type'],
                'amount': request_body['amount'],
                'phone': request_body['phone'],
            }
            parcel = ParcelSerializer(data=data)
            if parcel.is_valid():
                parcel.create(data)
            else:
                errors = parcel.errors
                errors_list = []
                for error in errors:
                    field = error
                    text = errors[error][0].title()
                    errors_list.append(f'Некорректно указаны данные в поле {field}. {text}')
                return HttpResponse(
                    json.dumps(
                        {'state': 'error', 'message': f'Некорректно указаны данные.',
                         'details': {'errors': errors_list},
                         'instance': request.path}, ensure_ascii=False), status=404)
        else:
            return HttpResponse(
                json.dumps(
                    {'state': 'error', 'message': f'Некорректно указано поле object.',
                     'details': {'message': 'Object должен быть равен 0 или 1.'},
                     'instance': request.path}, ensure_ascii=False), status=404)
        return HttpResponse(json.dumps({}, ensure_ascii=False), status=200)
    except KeyError as e:
        return HttpResponse(
            json.dumps(
                {'state': 'error', 'message': f'Не указано поле {e}.',
                 'details': {},
                 'instance': request.path}, ensure_ascii=False), status=404)
    except Exception as e:
        error = str(e) if DEBUG else ""
        return HttpResponse(
            json.dumps(
                {'state': 'error', 'message': f'Произошла непредвиденная ошибка.',
                 'details': {'error': error},
                 'instance': request.path}, ensure_ascii=False), status=404)


@swagger_auto_schema(method='PATCH', operation_summary="Выдать объект.",
                     manual_parameters=[id_param, object_param],
                     operation_description=operation_description,
                     responses=give_object_responses)
@api_view(["PATCH"])
def give_object(request):
    try:
        id_ = get_variable('id', request)
        if not id_is_valid(id_):
            return HttpResponse(
                json.dumps(
                    {'state': 'error', 'message': f'Некорректно указан id объекта.',
                     'details': {},
                     'instance': request.path}, ensure_ascii=False), status=400)
        object_type = get_variable('object', request)
        if object_type not in ['0', '1']:
            return HttpResponse(
                json.dumps(
                    {'state': 'error', 'message': f'Некорректно указан тип объекта.',
                     'details': {},
                     'instance': request.path}, ensure_ascii=False), status=400)
        if object_type == '0':
            object_ = Letter.objects.get(id=id_)
        else:
            object_ = Parcel.objects.get(id=id_)
        object_.is_given = True
        object_.save()
        return HttpResponse(json.dumps({}, ensure_ascii=False), status=200)
    except ObjectDoesNotExist as e:
        return HttpResponse(
            json.dumps(
                {'state': 'error', 'message': f'Объект не найден.',
                 'details': {},
                 'instance': request.path}, ensure_ascii=False), status=404)
    except Exception as e:
        error = str(e) if DEBUG else ""
        return HttpResponse(
            json.dumps(
                {'state': 'error', 'message': f'Произошла непредвиденная ошибка.',
                 'details': {'error': error},
                 'instance': request.path}, ensure_ascii=False), status=404)


@swagger_auto_schema(method='DELETE', operation_summary="Удалить объект.",
                     manual_parameters=[id_param, object_param],
                     operation_description=operation_description,
                     responses=delete_object_responses)
@api_view(["DELETE"])
def delete_object(request):
    try:
        id_ = get_variable('id', request)
        if not id_is_valid(id_):
            return HttpResponse(
                json.dumps(
                    {'state': 'error', 'message': f'Некорректно указан id объекта.',
                     'details': {},
                     'instance': request.path}, ensure_ascii=False), status=400)
        object_type = get_variable('object', request)
        if object_type not in ['0', '1']:
            return HttpResponse(
                json.dumps(
                    {'state': 'error', 'message': f'Некорректно указан тип объекта.',
                     'details': {},
                     'instance': request.path}, ensure_ascii=False), status=400)
        if object_type == '0':
            object_ = Letter.objects.get(id=id_)
        else:
            object_ = Parcel.objects.get(id=id_)
        object_.delete()
        return HttpResponse(json.dumps({}, ensure_ascii=False), status=200)
    except ObjectDoesNotExist as e:
        return HttpResponse(
            json.dumps(
                {'state': 'error', 'message': f'Объект не найден.',
                 'details': {},
                 'instance': request.path}, ensure_ascii=False), status=404)
    except Exception as e:
        error = str(e) if DEBUG else ""
        return HttpResponse(
            json.dumps(
                {'state': 'error', 'message': f'Произошла непредвиденная ошибка.',
                 'details': {'error': error},
                 'instance': request.path}, ensure_ascii=False), status=404)


@swagger_auto_schema(method='GET', operation_summary="Получить данные об объекте.",
                     manual_parameters=[id_param, object_param],
                     operation_description=operation_description,
                     responses=get_object_responses)
@api_view(["GET"])
def get_object(request):
    try:
        id_ = get_variable('id', request)
        if not id_is_valid(id_):
            return HttpResponse(
                json.dumps(
                    {'state': 'error', 'message': f'Некорректно указан id объекта.',
                     'details': {},
                     'instance': request.path}, ensure_ascii=False), status=400)
        object_type = get_variable('object', request)
        if object_type not in ['0', '1']:
            return HttpResponse(
                json.dumps(
                    {'state': 'error', 'message': f'Некорректно указан тип объекта.',
                     'details': {},
                     'instance': request.path}, ensure_ascii=False), status=400)
        if object_type == '0':
            object_ = Letter.objects.get(id=id_)
            data = {
                'sender': object_.sender,
                'receiver': object_.receiver,
                'point_of_dispatch': object_.point_of_dispatch,
                'point_of_receipt': object_.point_of_receipt,
                'index_dispatch': object_.index_dispatch,
                'index_receipt': object_.index_receipt,
                'letter_type': object_.letter_type,
                'weight': object_.weight,
                'is_given': object_.is_given,
            }
        else:
            object_ = Parcel.objects.get(id=id_)
            data = {
                'sender': object_.sender,
                'receiver': object_.receiver,
                'point_of_dispatch': object_.point_of_dispatch,
                'point_of_receipt': object_.point_of_receipt,
                'index_dispatch': object_.index_dispatch,
                'index_receipt': object_.index_receipt,
                'parcel_type': object_.letter_type,
                'amount': object_.weight,
                'phone': object_.weight,
                'is_given': object_.is_given,
            }
        return HttpResponse(json.dumps(data, ensure_ascii=False), status=200)
    except ObjectDoesNotExist as e:
        return HttpResponse(
            json.dumps(
                {'state': 'error', 'message': f'Объект не найден.',
                 'details': {},
                 'instance': request.path}, ensure_ascii=False), status=404)
    except Exception as e:
        error = str(e) if DEBUG else ""
        return HttpResponse(
            json.dumps(
                {'state': 'error', 'message': f'Произошла непредвиденная ошибка.',
                 'details': {'error': error},
                 'instance': request.path}, ensure_ascii=False), status=404)