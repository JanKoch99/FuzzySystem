import { Row, Col, Image } from "react-bootstrap";
import { useMemo } from "react";
import dataService from "../services/dataService.js";
import { getImageSrc } from "../utils/imageHelper";

export default function FinalSuggestion() {
  const images = useMemo(() => dataService.getFinalImages() || [], []);
  return (
    <div className="text-center">
      <h3>Final Suggestions</h3>
      <p>Pick your favorite gift idea:</p>
      <Row className="mt-3">
        {images.map((img, i) => (
          <Col key={i}>
            <Image
              src={getImageSrc(img.path)}
              thumbnail
              style={{ cursor: "pointer" }}
            />
          </Col>
        ))}
      </Row>
    </div>
  );
}
