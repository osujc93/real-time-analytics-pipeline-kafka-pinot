package blewy.models;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;

@JsonIgnoreProperties(ignoreUnknown = true)
public class Product {
    public String product_id;
    public String name;
    public String category;
    public double price;
    public boolean out_of_stock;
    public int stock;

    public Product() {
    }

    public Product(String product_id,
                   String name,
                   String category,
                   double price,
                   boolean out_of_stock,
                   int stock) {
        this.product_id = product_id;
        this.name = name;
        this.category = category;
        this.price = price;
        this.out_of_stock = out_of_stock;
        this.stock = stock;
    }
}
