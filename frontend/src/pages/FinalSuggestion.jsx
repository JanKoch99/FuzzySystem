import { Row, Col, Image } from "react-bootstrap";
import img1 from "../assets/img1.png";
import img2 from "../assets/img2.png";
import img3 from "../assets/img3.png";

export default function FinalSuggestion() {
    const images = [img1, img2, img3];
    return (
        <div className="text-center">
            <h3>Final Suggestions</h3>
            <p>Pick your favorite gift idea:</p>
            <Row className="mt-3">
                {images.map((img, i) => (
                    <Col key={i}>
                        <Image src={img} thumbnail style={{ cursor: "pointer" }} />
                    </Col>
                ))}
            </Row>
        </div>
    );
}
