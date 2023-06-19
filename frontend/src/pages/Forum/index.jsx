export default function Forum() {
    // TODO: fetch data
    const threads = [];

    return (<>
        <div class="breadcrumbs">
            <a href="{% url 'homepage' %}">Главная</a> > Форум
        </div>
        <div class="h1">
            <h1>Форум</h1>
        </div>
        <div>
            <ul class="list-articles">
                {threads.map(p =>
                    <div class="card">
                        <div class="card-content">
                            <h2 class="card-title">{p.title}</h2>
                            <p class="card-category">{p.topic_category_id}, от {p.user_id} </p>
                            <p class="card-date">{p.time_created}</p>
                            {p.last_comment_time &&
                                <p class="card-date">Последний комментарий: {p.last_comment_time} от {p.last_comment_author}</p>
                            }
                            <p class="card-text">{p.content}</p>
                            {/* TODO: provide url or make here */}
                            <a href="{ p.url }" class="card-link">Перейти к обсуждению</a>
                        </div>
                    </div>
                )}
            </ul>
        </div>
    </>)
}