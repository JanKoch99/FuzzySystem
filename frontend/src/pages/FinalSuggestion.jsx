import { Row, Col, Image } from "react-bootstrap";
import {useMemo} from "react";
import dataService from "../services/dataService.js";

export default function FinalSuggestion() {
    const images = useMemo(() => dataService.getFinalImages() || [], [])
    return (
        <div className="text-center">
            <h3>Final Suggestions</h3>
            <p>Pick your favorite gift idea:</p>
            <Row className="mt-3">
                {images.map((img, i) => (
                    <Col key={i}>
                        <Image src={img.path} thumbnail style={{ cursor: "pointer" }} />
                    </Col>
                ))}
            </Row>
        </div>
    );
}
