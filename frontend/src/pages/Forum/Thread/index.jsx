import { useParams } from 'react-router-dom';

export default function Thread() {
    const { threadUniqueName } = useParams();

    // TODO: fetch data and do 404 if not found
    const thread = {};
    const comments = [];

    // TODO: get data from state
    const user = {};

    // TODO: urls router using
    return (<>
        <div class="breadcrumbs">
            <a href="/* homepage */">Главная</a>
            <a href="{% url 'newspage' %}">Новости</a>
            {thread.title}
        </div>
        <div class="h1">
            <h1>{thread.title}</h1>
        </div>
        <div>
            <p>Категория: {thread.news_categories_id}</p>
            <p>Дата: {thread.time_created}</p>
        </div>
        {thread.photo &&
            <p><img src="{post.photo.url}" /></p>
        }
        <h2>{thread.title}</h2>
        {thread.content}

        <h2>Комментарии</h2>
        Всего комментариев: {comments.length}

        {user.is_authenticated &&
            <div>
                <p>Добавить комментарий</p>
                {/* TODO: make form */}
                <form method="post">
                    <button type="submit">Оставить комментарий</button>
                </form>
            </div>
        }

        <div>
            {comments.map(c =>
                <>
                    <h3>{c.user_id} - {c.time_created}</h3>
                    {c.content}
                </>
            )}
        </div>
    </>)
} 