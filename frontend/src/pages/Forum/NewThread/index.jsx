import { useEffect } from "react";
import { useNavigate } from "react-router-dom";

export default function NewThread() {
    const navigate = useNavigate();

    // TODO: get data from state
    const user = {};

    // TODO
    useEffect(() => {
        if (!user.isAuthenticated) {
            navigate('/forum');
        }
    }, [user.isAuthenticated])

    return (
        <div>
            <p>Новое обсуждение</p>
            <form method="post">
                {/* TODO: make form */}
                <button type="submit">Создать обсуждение</button>
            </form>
        </div>
    );
}