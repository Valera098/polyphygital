import './style.css';

export default function Layout({ children }) {
    let isAuthenticated = false;
    return (
        <>
            <header>
                <div class="logo-container">
                    <a href="{% url 'homepage' %}"> <img src="public/img/logo.png" alt="Главная" /> </a>
                </div>
                <nav>
                    <ul>
                        <li><a href="{% url 'newspage' %}">Новости</a></li>
                        <li><a href="{% url 'shedule' %}">Расписания</a></li>
                        <li><a href="{% url 'ratings' %}">Рейтинги</a></li>
                        <li><a href="{% url 'forum' %}">Форум</a></li>
                        <li><a href="#">Принять участие</a></li>
                        <li>
                            {
                                isAuthenticated ?
                                    <a href="#">Профиль</a> :
                                    <a href="#">Войти</a>
                            }
                        </li>
                    </ul>
                    <a href="#">
                        <div class="burger">
                        </div>
                    </a>
                </nav>
            </header>
            <div class="content">
                {children}
            </div>
            <footer>
                <div class="footer-content">
                    <div class="footer-links">
                        <ul>
                            <li><a href="#">ЧаВо</a></li>
                            <li><a href="#">О нас</a></li>
                            <li><a href="#">Команда</a></li>
                            <li><a href="#">Контакты</a></li>
                        </ul>
                    </div>
                    <div class="footer-links">
                        <ul>
                            <li><a href="https://fit.mospolytech.ru/">ФИТ</a></li>
                            <li><a href="https://mospolytech.ru/">Московский Политех</a></li>
                            <li><a href="https://gofuture.games/">Игры будущего</a></li>
                            <li><a href="https://phygitalsport.ru/">Федерация Фиджитал Спорта</a></li>
                        </ul>
                    </div>
                    <div class="map-container">
                        <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3173.003962971122!2d37.70804789492454!3d55.781904890556014!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x46b54ad610abc8a5%3A0xc42703145fe53a8d!2z0JzQvtGB0LrQvtCy0YHQutC40Lkg0L_QvtC70LjRgtC10YXQvdC40YfQtdGB0LrQuNC5INGD0L3QuNCy0LXRgNGB0LjRgtC10YI!5e0!3m2!1sru!2sru!4v1686701268051!5m2!1sru!2sru" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
                    </div>
                </div>
                <div class="copyright">
                    <p>Москва 2023. Все права защищены</p>
                </div>
            </footer>
        </>
    )
}
