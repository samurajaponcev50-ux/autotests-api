from clients.api_client import APIClient
from httpx import Response
from typing import TypedDict
from clients.private_http_builder import get_private_http_client, AuthenticationUserDict

class Exercise(TypedDict):
    """
    Описание структуры упражнения.
    """
    id: str
    title: str
    courseId: str
    maxScore: int | None
    minScore: int | None
    orderIndex: int
    description: str
    estimatedTime: str | None

class GetExerciseQueryDict(TypedDict):
    """
    Описание структуры запроса на получение списка упражнений.
    """
    exercise_id: str

class GetExercisesResponseDict(TypedDict):
    """
    Описание структуры ответа при получении списка упражнений.
    """
    exercises: list[Exercise]

class GetExerciseResponseDict(TypedDict):
    """
    Описание структуры ответа при получении конкретного упражнения.
    """
    exercise: Exercise

class CreateExerciseRequestDict(TypedDict):
    """
    Описание структуры запроса на создание упражнения.
    """
    title: str
    courseId: str
    maxScore: int | None
    minScore: int | None
    orderIndex: int
    description: str
    estimatedTime: str | None

class CreateExerciseResponseDict(TypedDict):
    """
    Описание структуры ответа при создании упражнения.
    """
    exercise: Exercise

class UpdateExerciseRequestDict(TypedDict):
    """
    Описание структуры запроса на редактирование упражнения.
    """
    title: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    description: str | None
    estimatedTime: str | None

class UpdateExerciseResponseDict(TypedDict):
    """
    Описание структуры ответа при обновлении упражнения.
    """
    exercise: Exercise

class DeleteExerciseResponseDict(TypedDict):
    """
    Описание структуры ответа при удалении упражнения.
    """
    str | None

class ExercisesClient(APIClient):
    """
    Клиент для работы с /api/v1/exercises
    """
    def get_exercises_api(self, query: GetExerciseQueryDict) -> Response:
        """
        Метод для получения списка упражнений.
        :param query: Словарь с exercise_id
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/exercises", params=query)

    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод для получение конкретного упражнения.
        :param exercise_id: Словарь с exercise_id
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/exercises/{exercise_id}")

    def create_exercise_api(self, request: CreateExerciseRequestDict) -> Response:
        """
        Метод для создания упражнения.
        :param request: Словарь с title, courseId, maxScore, minScore, orderIndex, description, estimatedTime.
        :return:Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/exercises/", json=request)

    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestDict) -> Response:
        """
        Метод редактирования упражнения.
        :param exercise_id: Словарь с exercise_id
        :param request: Словарь с title, maxScore, minScore, orderIndex, description, estimatedTime
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f"/api/v1/exercises/{exercise_id}", json=request)

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод удаления упражнения.
        :param exercise_id: Словарь с exercise_id
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/exercises/{exercise_id}")

    def get_exercises(self, request: GetExerciseQueryDict) -> GetExercisesResponseDict:
        """
        Метод для получения списка упражненияй инкапсулированный.
        :param request: Словарь с list[Exercise]
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        response = self.get_exercises_api(request)
        return response.json()

    def get_exercise(self, request: GetExerciseQueryDict) -> GetExerciseResponseDict:
        """
        Метод для получение конкретного упражнения инкапсулированный.
        :param request: Словарь с Exercise.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        response = self.get_exercise_api(request)
        return response.json()

    def create_exercise(self, request: CreateExerciseRequestDict) -> CreateExerciseResponseDict:
        """
        Метод для создания упражнения инкапсулированный.
        :param request: Словарь с title, courseId, maxScore, minScore, orderIndex, description, estimatedTime
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        response = self.create_exercise_api(request)
        return response.json()

    def update_exercise(self, request: UpdateExerciseRequestDict) -> UpdateExerciseResponseDict:
        """
        Метод для обновления упражнения инкапсулированный.
        :param request: Словарь с title, maxScore, minScore, orderIndex, description, estimatedTime
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        response = self.get_exercise_api(request)
        return response.json()

    def delete_exercise(self, request: GetExerciseQueryDict) -> DeleteExerciseResponseDict:
        """
        Метод для удаления упражнения инкапсулированный.
        :param request: Словарь с exercise_id
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        response = self.delete_exercise_api(request)
        return response.json()

def get_exercises_client(user: AuthenticationUserDict) -> ExercisesClient:
    """
    Функция создает экземпляр ExercisesClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию ExercisesClient.
    """
    return ExercisesClient(client=get_private_http_client(user))