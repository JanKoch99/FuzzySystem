import { Button, Card, Container } from "react-bootstrap";
import { useNavigate } from "react-router-dom";

export default function Home() {
    const navigate = useNavigate();

    return (
        <Container className="d-flex justify-content-center align-items-center" style={{ minHeight: "70vh" }}>
            <Card className="p-4 text-center shadow-sm bg-dark text-white border-white" style={{ maxWidth: "600px" }}>
                <h2 className="mb-3">Welcome to the Fuzzy Gift Recommender 🎁</h2>
                <p>
                    This app helps you find the perfect gift for someone special using
                    <strong> fuzzy logic </strong> — a smart way to balance factors like
                    age, budget, relationship, and personality.
                </p>

                <p>
                    You’ll go through a few quick steps:
                </p>
                <ol className="text-start mx-auto" style={{ maxWidth: "450px" }}>
                    <li>Enter your own details (age, budget, relationship, occasion).</li>
                    <li>Enter information about the person you’re buying for.</li>
                    <li>Pick your favorite image between pairs five times.</li>
                    <li>Get final gift suggestions and choose your favorite!</li>
                </ol>

                <p className="mt-3">
                    Ready to start your fuzzy logic journey?
                </p>

                <Button size="lg" onClick={() => navigate("/user")}>
                    Start Now
                </Button>
            </Card>
        </Container>
    );
}
