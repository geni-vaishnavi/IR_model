from ir_engine import calculate_ir

if __name__ == "__main__":
    industry = "Leather Products Manufacturing"
    ir_score = calculate_ir(industry)

    print(f"Industry: {industry}")
    print(f"Industry Risk (IR) Score: {ir_score}")
