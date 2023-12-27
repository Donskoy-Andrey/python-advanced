import abc
import asyncio


class AbstractModel:
    @abc.abstractmethod
    def compute(self):
        ...


class Handler:
    def __init__(self, model: AbstractModel):
        self._model = model

    async def handle_request(self) -> None:
        # Модель выполняет некий тяжёлый код (ознакомьтесь с ним в файле тестов),
        # вам необходимо добиться его эффективного конкурентного исполнения.
        #
        # Тест проверяет, что время исполнения одной корутины handle_request не слишком сильно
        # отличается от времени исполнения нескольких таких корутин, запущенных конкурентно.

        loop = asyncio.get_running_loop()
        await loop.run_in_executor(None, self._model.compute)
