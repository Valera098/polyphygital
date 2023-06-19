import PropTypes from 'prop-types';

import './style.css';

Layout.propTypes = {
  children: PropTypes.node.isRequired,
}

export default function Layout({ children }) {
    let isAuthenticated = false;
    return (
        <>
            <header>
                <div className="logo-container">
                    <a href=""> <img src="/public/img/logo.png" alt="Главная" /> </a>
                </div>
                <nav>
                    <ul>
                        <li><a href="">Новости</a></li>
                        <li><a href="">Расписания</a></li>
                        <li><a href="">Рейтинги</a></li>
                        <li><a href="">Форум</a></li>
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
                        <div className="burger">
                        </div>
                    </a>
                </nav>
            </header>
            <div className="content">
                {children}
            </div>
            <footer>
                <div className="footer-content">
                    <div className="footer-links">
                        <ul>
                            <li><a href="#">ЧаВо</a></li>
                            <li><a href="#">О нас</a></li>
                            <li><a href="#">Команда</a></li>
                            <li><a href="#">Контакты</a></li>
                        </ul>
                    </div>
                    <div className="footer-links">
                        <ul>
                            <li><a href="https://fit.mospolytech.ru/">ФИТ</a></li>
                            <li><a href="https://mospolytech.ru/">Московский Политех</a></li>
                            <li><a href="https://gofuture.games/">Игры будущего</a></li>
                            <li><a href="https://phygitalsport.ru/">Федерация Фиджитал Спорта</a></li>
                        </ul>
                    </div>
                    <div className="map-container">
                        <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3173.003962971122!2d37.70804789492454!3d55.781904890556014!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x46b54ad610abc8a5%3A0xc42703145fe53a8d!2z0JzQvtGB0LrQvtCy0YHQutC40Lkg0L_QvtC70LjRgtC10YXQvdC40YfQtdGB0LrQuNC5INGD0L3QuNCy0LXRgNGB0LjRgtC10YI!5e0!3m2!1sru!2sru!4v1686701268051!5m2!1sru!2sru" width="400" height="300" style={{border:0}} allowFullScreen="" loading="lazy" referrerPolicy="no-referrer-when-downgrade"></iframe>
                    </div>
                </div>
                <div className="copyright">
                    <p>Москва 2023. Все права защищены</p>
                </div>
            </footer>
        </>
    )
}
