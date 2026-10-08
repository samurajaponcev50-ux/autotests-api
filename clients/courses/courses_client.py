from clients.api_client import APIClient
from clients.private_http_builder import get_private_http_client, AuthenticationUserDict
from httpx import Response
from typing import TypedDict


class GetCoursesQueryDict(TypedDict):
    """
    Описание структуры запроса на получение списка курсов.
    """
    userId: str

class CreateCourseRequest(TypedDict):
    """
    Описание структуры запроса на создание курса.
    """
    title: str
    maxScore: int
    minScore: int
    description: str
    estimatedTime: str
    previewFileId: str
    createdByUserId: str

class UpdateCourseRequestDict(TypedDict):
    """
    Описание структуры запроса на обновление курса.
    """
    title: str | None
    maxScore: int | None
    minScore: int | None
    description: str | None
    estimatedTime: str | None

class CoursesClient(APIClient):
    """
    Клиент для работы с /api/v1/courses
    """
    def get_courses_api(self, query: GetCoursesQueryDict) -> Response:
        """
        Метод для получения списка курсов
        :param query: Словарь с userId
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/courses", params=query)

    def get_course_api(self, course_id: str) -> Response:
        """
        Метод для получения конкретного курса
        :param course_id: Словарь с userId
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/courses/{course_id}")

    def create_course_api(self, request:CreateCourseRequest) -> Response:
        """
        Метод для создания курса
        :param request: Словарь с title, maxScore, minScore, description, estimatedTime, previewFileId, createdByUserId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/courses", json=request)

    def update_course_api(self, course_id: str, request: UpdateCourseRequestDict) -> Response:
        """
        Метод для обновления курса
        :param course_id: Идентификатор курса
        :param request: Словарь с title, maxScore, minScore, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f"/api/v1/courses{course_id}", json=request)


    def delete_course_api(self, course_id: str) -> Response:
        """
        Метод для удаления курса
        :param course_id: Идентификатор курса.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/courses/{course_id}")

def get_courses_client(user: AuthenticationUserDict) -> CoursesClient:
    """
    Функциоя создает экземпляр CoursesClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию CoursesClient.
    """
    return CoursesClient(client=get_private_http_client(user))