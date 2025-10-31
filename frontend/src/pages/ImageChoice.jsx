import { useState } from "react";
import { Row, Col, Image } from "react-bootstrap";
import { useNavigate } from "react-router-dom";
import img1 from "../assets/img1.png";
import img2 from "../assets/img2.png";
import img3 from "../assets/img3.png";

const imagePairs = [
    [img1, img2],
    [img2, img3],
    [img1, img3],
    [img2, img1],
    [img3, img2],
];

export default function ImageChoice() {
    const [round, setRound] = useState(0);
    const navigate = useNavigate();

    const handleChoice = () => {
        if (round < 4) setRound(round + 1);
        else navigate("/suggestion");
    };

    return (
        <div className="text-center">
            <h3>Choose your preferred image (Round {round + 1}/5)</h3>
            <Row className="mt-4">
                <Col>
                    <Image
                        src={imagePairs[round][0]}
                        thumbnail
                        style={{ cursor: "pointer" }}
                        onClick={handleChoice}
                    />
                </Col>
                <Col>
                    <Image
                        src={imagePairs[round][1]}
                        thumbnail
                        style={{ cursor: "pointer" }}
                        onClick={handleChoice}
                    />
                </Col>
            </Row>
        </div>
    );
}
