class CreateQueries < ActiveRecord::Migration
  def change
    create_table :queries do |t|
      t.string :name
      t.text :description
      t.text :info
      t.datetime :created_at
      t.timestamps null: false
    end
  end
end
