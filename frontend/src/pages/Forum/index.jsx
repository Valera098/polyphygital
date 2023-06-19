export default function Forum() {
    // TODO: fetch data
    const threads = [];

    // TODO: urls
    return (<>
        <div className="breadcrumbs">
            <a href="">Главная</a>
            <a href="">Форум</a>
        </div>
        <div className="h1">
            <h1>Форум</h1>
        </div>
        <div>
            <ul className="list-articles">
                {threads.map(p =>
                    <div className="card" key={p.id}>
                        <div className="card-content">
                            <h2 className="card-title">{p.title}</h2>
                            <p className="card-category">{p.topic_category_id}, от {p.user_id} </p>
                            <p className="card-date">{p.time_created}</p>
                            {p.last_comment_time &&
                                <p className="card-date">Последний комментарий: {p.last_comment_time} от {p.last_comment_author}</p>
                            }
                            <p className="card-text">{p.content}</p>
                            {/* TODO: provide url or make here */}
                            <a href="{ p.url }" className="card-link">Перейти к обсуждению</a>
                        </div>
                    </div>
                )}
            </ul>
        </div>
    </>)
}