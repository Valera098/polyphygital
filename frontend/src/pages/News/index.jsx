import { useLoaderData } from 'react-router-dom';
import './style.css';

export default function News() {
    // TODO: fetch data
    const posts = useLoaderData();
    console.log(posts);
    return (<>
        <div className="breadcrumbs">
            <a href="">Главная</a>
            Новости
        </div>
        <div className="h1">
            <h1>Новостной блок</h1>
        </div>
        <div>
            <ul className="list-articles">
                {posts.map(p =>
                    <div className="card" key={p.id}>
                        <div className="card-image">
                            {p.image ?
                                <img src="{{p.image.url}}" /> :
                                <img src="public/img/placeholder.jpeg" />
                            }
                        </div>
                        <div className="card-content">
                            <h2 className="card-title">{p.title}</h2>
                            <p className="card-category">Категория: {p.news_categories_id} </p>
                            <p className="card-date">{p.time_created}</p>
                            <p className="card-text">{p.content}</p>
                            {/* TODO: provide url or make here */}
                            <a href="{ p.url }" className="card-link">Читать новость</a>
                        </div>
                    </div>
                )}
            </ul>
        </div>
    </>);
}
