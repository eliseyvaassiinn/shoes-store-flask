from flask import Flask
from app.controllers.task_controller import TaskController

def create_app():
    app = Flask(__name__, template_folder='views/templates')
    app.secret_key = 'super-secret-key-for-flash' # Flask зберігає flash-повідомлення
    # не в базі даних і не в пам'яті сервера, а в cookie браузера користувача (в сесії).
    # cесія в Flask — це підписаний (signed) словник, який зберігається в cookie.
    # підпис робиться за допомогою секретного ключа (secret_key).
    # без секретного ключа Flask не може створити безпечну сесію, а значить не може зберегти flash-повідомлення

    # екземпляр контролера
    controller = TaskController()

    # реєстрація маршрутів та їх обробників
    @app.route('/', methods=['GET'])
    def index():
        return controller.index()

    @app.route('/tasks', methods=['POST'])
    def store():
        return controller.store()

    @app.route('/tasks/<int:task_id>/done', methods=['POST'])
    def mark_done(task_id):
        return controller.mark_done(task_id)

    @app.route('/tasks/<int:task_id>/delete', methods=['POST'])
    def delete(task_id):
        return controller.delete(task_id)

    return app