from drf_yasg import openapi

object_param = openapi.Parameter("object", in_=openapi.IN_QUERY, type=openapi.TYPE_INTEGER,
                                 operation_description='Тип объекта', example=0)
id_param = openapi.Parameter("id", in_=openapi.IN_QUERY, type=openapi.TYPE_INTEGER,
                             operation_description='ID объекта', example=0)

get_objects_response_200 = openapi.Schema(type=openapi.TYPE_OBJECT,
                                          properties={
                                              "letters": openapi.Schema(
                                                  type=openapi.TYPE_OBJECT,
                                                  properties={
                                                      "id": openapi.Schema(type=openapi.TYPE_INTEGER, example=0),
                                                      "sender": openapi.Schema(type=openapi.TYPE_STRING,
                                                                               example="Иванов Иван Иванович"),
                                                      "receiver": openapi.Schema(type=openapi.TYPE_STRING,
                                                                                 example="Иванов Иван Иванович"),
                                                      "point_of_dispatch": openapi.Schema(type=openapi.TYPE_STRING,
                                                                                          example="Пункт отправления"),
                                                      "point_of_receipt": openapi.Schema(type=openapi.TYPE_STRING,
                                                                                         example="Пункт получения"),
                                                      "index_dispatch": openapi.Schema(type=openapi.TYPE_INTEGER,
                                                                                       example=12345),
                                                      "index_receipt": openapi.Schema(type=openapi.TYPE_INTEGER,
                                                                                      example=54321),
                                                      "letter_type": openapi.Schema(type=openapi.TYPE_INTEGER,
                                                                                    example=0),
                                                      "weight": openapi.Schema(type=openapi.TYPE_INTEGER, example=10),
                                                      "is_given": openapi.Schema(type=openapi.TYPE_BOOLEAN,
                                                                                 example=False),
                                                  }
                                              ),
                                              "parcels": openapi.Schema(
                                                  type=openapi.TYPE_ARRAY,
                                                  items=openapi.Schema(
                                                      type=openapi.TYPE_OBJECT,
                                                      properties={
                                                          "id": openapi.Schema(type=openapi.TYPE_INTEGER, example=0),
                                                          "sender": openapi.Schema(type=openapi.TYPE_STRING,
                                                                                   example="Иванов Иван Иванович"),
                                                          "receiver": openapi.Schema(type=openapi.TYPE_STRING,
                                                                                     example="Иванов Иван Иванович"),
                                                          "point_of_dispatch": openapi.Schema(type=openapi.TYPE_STRING,
                                                                                              example="Пункт отправления"),
                                                          "point_of_receipt": openapi.Schema(type=openapi.TYPE_STRING,
                                                                                             example="Пункт получения"),
                                                          "index_dispatch": openapi.Schema(type=openapi.TYPE_INTEGER,
                                                                                           example=12345),
                                                          "index_receipt": openapi.Schema(type=openapi.TYPE_INTEGER,
                                                                                          example=54321),
                                                          "parcel_type": openapi.Schema(type=openapi.TYPE_INTEGER,
                                                                                        example=0),
                                                          "amount": openapi.Schema(type=openapi.TYPE_INTEGER,
                                                                                   example=1000),
                                                          "phone": openapi.Schema(type=openapi.TYPE_STRING,
                                                                                  example="89150000000"),
                                                          "is_given": openapi.Schema(type=openapi.TYPE_BOOLEAN,
                                                                                     example=False),
                                                      })),
                                          })

get_object_response_200 = openapi.Schema(type=openapi.TYPE_OBJECT,
                                         properties={
                                             "sender": openapi.Schema(type=openapi.TYPE_STRING,
                                                                      example="Иванов Иван Иванович"),
                                             "receiver": openapi.Schema(type=openapi.TYPE_STRING,
                                                                        example="Иванов Иван Иванович"),
                                             "point_of_dispatch": openapi.Schema(type=openapi.TYPE_STRING,
                                                                                 example="Пункт отправления"),
                                             "point_of_receipt": openapi.Schema(type=openapi.TYPE_STRING,
                                                                                example="Пункт получения"),
                                             "index_dispatch": openapi.Schema(type=openapi.TYPE_INTEGER,
                                                                              example=12345),
                                             "index_receipt": openapi.Schema(type=openapi.TYPE_INTEGER,
                                                                             example=54321),
                                             "parcel_type": openapi.Schema(type=openapi.TYPE_INTEGER, example=0),
                                             "letter_type": openapi.Schema(type=openapi.TYPE_INTEGER, example=0),
                                             "amount": openapi.Schema(type=openapi.TYPE_INTEGER,
                                                                      example=1000),
                                             "phone": openapi.Schema(type=openapi.TYPE_STRING,
                                                                     example="89150000000"),
                                             "weight": openapi.Schema(type=openapi.TYPE_INTEGER,
                                                                      example=10),
                                             "is_given": openapi.Schema(type=openapi.TYPE_BOOLEAN,
                                                                        example=False),
                                         })

create_object_request_body = openapi.Schema(type=openapi.TYPE_OBJECT,
                                            required=['object', 'sender', 'receiver',
                                                      'point_of_dispatch', 'point_of_receipt', 'index_dispatch',
                                                      'parcel_type', 'letter_type', 'amount', 'phone', 'weight'],
                                            properties={
                                                "sender": openapi.Schema(type=openapi.TYPE_STRING,
                                                                         example="Иванов Иван Иванович"),
                                                "receiver": openapi.Schema(type=openapi.TYPE_STRING,
                                                                           example="Иванов Иван Иванович"),
                                                "point_of_dispatch": openapi.Schema(type=openapi.TYPE_STRING,
                                                                                    example="Пункт отправления"),
                                                "point_of_receipt": openapi.Schema(type=openapi.TYPE_STRING,
                                                                                   example="Пункт получения"),
                                                "index_dispatch": openapi.Schema(type=openapi.TYPE_INTEGER,
                                                                                 example=12345),
                                                "index_receipt": openapi.Schema(type=openapi.TYPE_INTEGER,
                                                                                example=54321),
                                                "parcel_type": openapi.Schema(type=openapi.TYPE_INTEGER, example=0),
                                                "letter_type": openapi.Schema(type=openapi.TYPE_INTEGER, example=0),
                                                "amount": openapi.Schema(type=openapi.TYPE_INTEGER,
                                                                         example=1000),
                                                "phone": openapi.Schema(type=openapi.TYPE_STRING,
                                                                        example="89150000000"),
                                                "weight": openapi.Schema(type=openapi.TYPE_INTEGER,
                                                                         example=10),
                                            })

delete_object_response_200 = openapi.Schema(type=openapi.TYPE_OBJECT)
give_object_response_200 = openapi.Schema(type=openapi.TYPE_OBJECT)
create_object_response_200 = openapi.Schema(type=openapi.TYPE_OBJECT)
get_objects_responses = {200: get_objects_response_200}
delete_object_responses = {200: delete_object_response_200}
give_object_responses = {200: give_object_response_200}
create_object_responses = {200: create_object_response_200}
get_object_responses = {200: get_object_response_200}

operation_description = 'Object: 0 - Письмо, 1 - Посылка.'
