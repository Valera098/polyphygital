import { useParams } from 'react-router-dom';

export default function Post() {
    const { postUniqueName } = useParams();

    // TODO: fetch data and do 404 if not found
    const post = {};
    const comments = [];

    // TODO: get data from state
    const user = {};

    // TODO: urls router using
    return (<>
        <div className="breadcrumbs">
            <a href="">Главная</a>
            <a href="">Новости</a>
            {post.title}
        </div>
        <div className="h1">
            <h1>{post.title}</h1>
        </div>
        <div>
            <p>Категория: {post.news_categories_id}</p>
            <p>Дата: {post.time_created}</p>
        </div>
        {post.photo &&
            <p><img src="{post.photo.url}" /></p>
        }
        <h2>{post.title}</h2>
        {post.content}

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